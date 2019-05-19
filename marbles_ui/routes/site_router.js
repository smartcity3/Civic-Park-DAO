'use strict';
/* global process */
/*******************************************************************************
 * Copyright (c) 2015 IBM Corp.
 *
 * All rights reserved.
 *
 *******************************************************************************/
var express = require('express');
var cachebust_js = Date.now();
var cachebust_css = Date.now();

module.exports = function (logger) { // PREV: (logger, cp) {
	var cp = null;
	var app = express();

	// ============================================================================================================================
	// Root
	// ============================================================================================================================
	app.get('/', function (req, res) {
		res.redirect('/home');
	});

	// ============================================================================================================================
	// Login
	// ============================================================================================================================
	app.get('/login', function (req, res) {
		res.render('login', { title: 'Marbles - Login', bag: build_bag(req) });
	});

	app.post('/login', function (req, res) {
		req.session.user = { username: 'Admin' };
		res.redirect('/home');
	});

	app.get('/logout', function (req, res) {
		req.session.destroy();
		res.redirect('/login');
	});


	// ============================================================================================================================
	// Home
	// ============================================================================================================================
	app.get('/home', function (req, res) {
		route_me(req, res);
	});

	app.get('/create', function (req, res) {
		route_me(req, res);
	});

	function route_me(req, res) {
		//if (!req.session.user || !req.session.user.username) {		// no session? send them to login
		//	res.redirect('/login');
		//} else {
		res.render('marbles', { title: 'Marbles - Home', bag: build_bag(req) });
		//}
	}

	//anything in here gets passed to the Pug template engine
	function build_bag(req) {
		return {
			e: process.error,							//send any setup errors
			config_filename: "test filename",
			cp_filename: "test", // cp.config.cred_filename,
			jshash: cachebust_js,						//js cache busting hash (not important)
			csshash: cachebust_css,						//css cache busting hash (not important)
			marble_company: process.env.marble_company,
			creds: get_mock_credential_data(),  // PREV: get_credential_data(),
			using_env: "dev-test"// cp.using_env,
		};
	}

	function get_mock_credential_data() {
		// const channel = cp.getChannelId();
		// const first_org = cp.getClientOrg();
		// const first_ca = cp.getFirstCaName(first_org);
		// const first_peer = cp.getFirstPeerName(channel);
		// const first_orderer = cp.getFirstOrdererName(channel);
		var ret = {
			admin_id: null, // cp.getEnrollObj(first_ca, 0).enrollId,
			admin_secret: null, // cp.getEnrollObj(first_ca, 0).enrollSecret,
			orderer: null, // cp.getOrderersUrl(first_orderer),
			ca: null, // cp.getCasUrl(first_ca),
			peer: null, // cp.getPeersUrl(first_peer),
			chaincode_id: null, // cp.getChaincodeId(),
			channel: null, // cp.getChannelId(),
			chaincode_version: null, // cp.getChaincodeVersion(),
			marble_owners: null // cp.getMarbleUsernames(),
		};
		for (var i in ret) {
			if (ret[i] == null) ret[i] = '';			//set to blank if not found
		}
		return ret;
	}

	//get cred data
	function get_credential_data() {
		const channel = cp.getChannelId();
		const first_org = cp.getClientOrg();
		const first_ca = cp.getFirstCaName(first_org);
		const first_peer = cp.getFirstPeerName(channel);
		const first_orderer = cp.getFirstOrdererName(channel);
		var ret = {
			admin_id: cp.getEnrollObj(first_ca, 0).enrollId,
			admin_secret: cp.getEnrollObj(first_ca, 0).enrollSecret,
			orderer: cp.getOrderersUrl(first_orderer),
			ca: cp.getCasUrl(first_ca),
			peer: cp.getPeersUrl(first_peer),
			chaincode_id: cp.getChaincodeId(),
			channel: cp.getChannelId(),
			chaincode_version: cp.getChaincodeVersion(),
			marble_owners: cp.getMarbleUsernames(),
		};
		for (var i in ret) {
			if (ret[i] == null) ret[i] = '';			//set to blank if not found
		}
		return ret;
	}

	return app;
};
