# Makefile for source rpm: setup
# $Id$
NAME := setup
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
