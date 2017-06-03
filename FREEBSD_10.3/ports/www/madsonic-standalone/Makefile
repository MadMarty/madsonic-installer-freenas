# Created by: Jeremie Le Hen <jlh@FreeBSD.org>
# Based on www/subsonic-standalone
#
# $FreeBSD$
#

PORTNAME=	madsonic-standalone
PORTVERSION=	6.3
BUILDVERSION=	9500
DISTDATE=	20170602
PORTREVISION=	5
CATEGORIES=	www java
MASTER_SITES=	http://madsonic.org/download/${PORTVERSION}/
DISTNAME=	${DISTDATE}_madsonic-${PORTVERSION}.${BUILDVERSION}-standalone

MAINTAINER=	mkappdev@madsonic.org
COMMENT=	Madsonic streaming media server, standalone version

LICENSE=	GPLv3

OPTIONS_GROUP=	TRANSCODING
TRANSCODING_DESC=	Transcoding support
OPTIONS_GROUP_TRANSCODING=	FFMPEG FLAC LAME VORBIS FAAC FAAD XMP MPC APE
FFMPEG_DESC=	Depend on FFmpeg for audio and video transcoding
VORBIS_DESC=	Depend on oggenc/oggdec for Vorbis transcoding
FLAC_DESC=	Depend on FLAC for transcoding
LAME_DESC=	Depend on LAME for MP3 transcoding
FAAC_DESC=	Depend on FAAD for AAC/M4A transcoding
FAAD_DESC=	Depend on FAAC for AAC/M4A transcoding
XMP_DESC=	Depend on XMP for module file transcoding
APE_DESC=	Depend on mac for Monkeys Audio transcoding
MPC_DESC=	Depend on mpcdec for MPC transcoding

OPTIONS_DEFAULT=	FFMPEG
OPTIONS_SUB=	yes

FFMPEG_RUN_DEPENDS=	ffmpeg:multimedia/ffmpeg
FLAC_RUN_DEPENDS=	flac:audio/flac
LAME_RUN_DEPENDS=	lame:audio/lame
VORBIS_RUN_DEPENDS=	oggenc:audio/vorbis-tools
FAAC_RUN_DEPENDS=	faac:audio/faac
FAAD_RUN_DEPENDS=	faad:audio/faad
XMP_RUN_DEPENDS=	xmp:audio/xmp
APE_RUN_DEPENDS=	mac:audio/mac
MPC_RUN_DEPENDS=	mpcdec:audio/musepack

.include <bsd.port.options.mk>

NO_WRKSUBDIR=	yes
NO_BUILD=	yes
USE_JAVA=	yes
USE_RC_SUBR=	madsonic
JAVA_VERSION=	1.7+
JAVA_RUN=	yes

# Don't waste UID/GID and reuse media's user.
USERS=		media
GROUPS=		media

# Keep the same variable names as in the Madsonic port to minimize diffs.
MADSONIC_HOME=	/var/madsonic
PLIST_SUB+=	MADSONIC_HOME="${MADSONIC_HOME}" \
		USER="${USERS}" \
		GROUP="${GROUPS}"
SUB_FILES=	pkg-message \
		message-transcoding
SUB_LIST=	MADSONIC_HOME="${MADSONIC_HOME}" \
		USER="${USERS}" \
		GROUP="${GROUPS}" \
		JAVA="${JAVA}"

CONFLICTS_INSTALL=	madsonic-jetty madsonic-tomcat[678]

do-install:
	@${CAT} ${PKGDIR}/pkg-message-spacer >> ${PKGMESSAGE}
	@${CAT} ${WRKDIR}/message-transcoding >> ${PKGMESSAGE}
	@${CAT} ${PKGDIR}/pkg-message-spacer >> ${PKGMESSAGE}
	${MKDIR} ${STAGEDIR}${DATADIR}
	${INSTALL_DATA} ${WRKSRC}/madsonic.war ${STAGEDIR}${DATADIR}/
	${INSTALL_DATA} ${WRKSRC}/madsonic-booter.jar ${STAGEDIR}${DATADIR}/

post-install:
	${MKDIR} ${STAGEDIR}${MADSONIC_HOME}/transcode

post-install-FFMPEG-on:
	${LN} -sf ${PREFIX}/bin/ffmpeg ${STAGEDIR}${MADSONIC_HOME}/transcode/ffmpeg

post-install-FLAC-on:
	${LN} -sf ${PREFIX}/bin/flac ${STAGEDIR}${MADSONIC_HOME}/transcode/flac

post-install-LAME-on:
	${LN} -sf ${PREFIX}/bin/lame ${STAGEDIR}${MADSONIC_HOME}/transcode/lame

.include <bsd.port.mk>
