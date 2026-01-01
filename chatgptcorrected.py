import requests
import datetime
import time

# ===========================================
# CONFIG
# ===========================================
# PAIRS = [
#     "B-BTC_USDT","B-ETH_USDT","B-MKR_USDT","B-BNB_USDT","B-SOL_USDT",
#     "B-XRP_USDT","B-ADA_USDT","B-DOT_USDT","B-LINK_USDT","B-AVAX_USDT",
#     "B-MATIC_USDT","B-UNI_USDT","B-ATOM_USDT","B-APT_USDT","B-OP_USDT",
#     "B-AR_USDT","B-ICP_USDT","B-FTM_USDT","B-NEAR_USDT","B-SEI_USDT"
# ]
PAIRS=["B-HYPE_USDT","B-CLANKER_USDT","B-DASH_USDT","B-GIGGLE_USDT","B-QNT_USDT","B-LTC_USDT","B-SOL_USDT","B-AAVE_USDT","B-TAO_USDT","B-XMR_USDT","B-ZEC_USDT","B-BCH_USDT","B-BNB_USDT","B-ETH_USDT","B-COMP_USDT","B-TRB_USDT","B-BSV_USDT","B-AVAX_USDT","B-LINK_USDT","B-ETC_USDT","B-OG_USDT","B-ENS_USDT","B-NMR_USDT","B-ZEN_USDT","B-PROM_USDT","B-TRUMP_USDT","B-XRP_USDT","B-BTC_USDT","B-PAXG_USDT","B-YFI_USDT"
"B-GMX_USDT","B-KSM_USDT","B-BANANA_USDT","B-UNI_USDT","B-EGLD_USDT","B-ILV_USDT","B-AUCTION_USDT","B-METIS_USDT","B-MLN_USDT""B-INJ_USDT","B-XVS_USDT","B-ORDI_USDT","B-SSV_USDT""B-NEO_USDT","B-DEXE_USDT","B-EUL_USDT","B-LPT_USDT","B-ICP_USDT","B-MOVR_USDT","B-VANA_USDT","B-GAS_USDT","B-ATOM_USDT","B-CAKE_USDT","B-PENDLE_USDT","B-RPL_USDT","B-DOT_USDT","B-SANTOS_USDT","B-IP_USDT","B-VVV_USDT","B-APT_USDT","B-TON_USDT","B-ASR_USDT","B-NEAR_USDT",]
# PAIRS=[
#     "B-ROSE_USDT",
#     "B-LTC_USDT",
#     "B-TRX_USDT",
#     "B-STG_USDT",
#     "B-BMT_USDT",
#     "B-LUNA2_USDT",
#     "B-BANANAS31_USDT",
#     "B-MAVIA_USDT",
#     "B-XLM_USDT",
#     "B-ALICE_USDT",
#     "B-CFX_USDT",
#     "B-PAXG_USDT",
#     "B-MLN_USDT",
#     "B-ACH_USDT",
#     "B-GUN_USDT",
#     "B-VELODROME_USDT",
#     "B-IOTA_USDT",
#     "B-STO_USDT",
#     "B-JST_USDT",
#     "B-BTC_USDT",
#     "B-DOLO_USDT",
#     "B-USDC_USDT",
#     "B-VANA_USDT",
#     "B-PYTH_USDT",
#     "B-ASR_USDT",
#     "B-ETH_USDT",
#     "B-APE_USDT",
#     "B-HUMA_USDT",
#     "B-QTUM_USDT",
#     "B-ARB_USDT",
#     "B-SOPH_USDT",
#     "B-AUCTION_USDT",
#     "B-HYPE_USDT",
#     "B-TLM_USDT",
#     "B-LA_USDT",
#     "B-RESOLV_USDT",
#     "B-THETA_USDT",
#     "B-F_USDT",
#     "B-SAHARA_USDT",
#     "B-PUMP_USDT",
#     "B-KNC_USDT",
#     "B-MAV_USDT",
#     "B-ARKM_USDT",
#     "B-OXT_USDT",
#     "B-SNX_USDT",
#     "B-BICO_USDT",
#     "B-BIGTIME_USDT",
#     "B-WAXP_USDT",
#     "B-TUT_USDT",
#     "B-GAS_USDT",
#     "B-OG_USDT",
#     "B-TREE_USDT",
#     "B-PROVE_USDT",
#     "B-NXPC_USDT",
#     "B-WOO_USDT",
#     "B-POWR_USDT",
#     "B-CAKE_USDT",
#     "B-ICP_USDT",
#     "B-ETHW_USDT",
#     "B-ERA_USDT",
#     "B-1000SATS_USDT",
#     "B-TOWNS_USDT",
#     "B-XPL_USDT",
#     "B-MITO_USDT",
#     "B-DRIFT_USDT",
#     "B-HEMI_USDT",
#     "B-LINEA_USDT",
#     "B-MOVR_USDT",
#     "B-OPEN_USDT",
#     "B-1000CAT_USDT",
#     "B-NFP_USDT",
#     "B-APT_USDT",
#     "B-ZIL_USDT",
#     "B-AI_USDT",
#     "B-SKY_USDT",
#     "B-WIF_USDT",
#     "B-MUBARAK_USDT",
#     "B-ALT_USDT",
#     "B-AVNT_USDT",
#     "B-BCH_USDT",
#     "B-HOLO_USDT",
#     "B-SUI_USDT",
#     "B-XRP_USDT",
#     "B-ZKC_USDT",
#     "B-ACT_USDT",
#     "B-0G_USDT",
#     "B-BARD_USDT",
#     "B-TON_USDT",
#     "B-POPCAT_USDT",
#     "B-LINK_USDT",
#     "B-VANRY_USDT",
#     "B-BAN_USDT",
#     "B-ADA_USDT",
#     "B-DASH_USDT",
#     "B-ASTER_USDT",
#     "B-BNB_USDT",
#     "B-ETHFI_USDT",
#     "B-W_USDT",
#     "B-FF_USDT",
#     "B-ATOM_USDT",
#     "B-TNSR_USDT",
#     "B-MOVE_USDT",
#     "B-EDEN_USDT",
#     "B-ONT_USDT",
#     "B-PUNDIX_USDT",
#     "B-NOM_USDT",
#     "B-ME_USDT",
#     "B-BAT_USDT",
#     "B-ATH_USDT",
#     "B-VET_USDT",
#     "B-NEO_USDT",
#     "B-2Z_USDT",
#     "B-SAGA_USDT",
#     "B-YB_USDT",
#     "B-IOST_USDT",
#     "B-CC_USDT",
#     "B-ALGO_USDT",
#     "B-HYPER_USDT",
#     "B-KAVA_USDT",
#     "B-STABLE_USDT",
#     "B-TAO_USDT",
#     "B-REZ_USDT",
#     "B-RLC_USDT",
#     "B-WET_USDT",
#     "B-ALPINE_USDT",
#     "B-NIGHT_USDT",
#     "B-SOL_USDT",
#     "B-QNT_USDT",
#     "B-ZKP_USDT",
#     "B-CRV_USDT",
#     "B-DIA_USDT",
#     "B-TRB_USDT",
#     "B-SUPER_USDT",
#     "B-SUSHI_USDT",
#     "B-EGLD_USDT",
#     "B-ZEREBRO_USDT",
#     "B-AVAX_USDT",
#     "B-AWE_USDT",
#     "B-ENJ_USDT",
#     "B-KSM_USDT",
#     "B-NEAR_USDT",
#     "B-MBOX_USDT",
#     "B-PROM_USDT",
#     "B-FIL_USDT",
#     "B-RSR_USDT",
#     "B-BEL_USDT",
#     "B-POL_USDT",
#     "B-ZEN_USDT",
#     "B-SKL_USDT",
#     "B-1MBABYDOGE_USDT",
#     "B-FIDA_USDT",
#     "B-FIO_USDT",
#     "B-NEWT_USDT",
#     "B-RVN_USDT",
#     "B-HMSTR_USDT",
#     "B-CHZ_USDT",
#     "B-MOODENG_USDT",
#     "B-SAFE_USDT",
#     "B-SAND_USDT",
#     "B-SANTOS_USDT",
#     "B-COW_USDT",
#     "B-ONE_USDT",
#     "B-COTI_USDT",
#     "B-MTL_USDT",
#     "B-CETUS_USDT",
#     "B-SOMI_USDT",
#     "B-GTC_USDT",
#     "B-CHR_USDT",
#     "B-DYDX_USDT",
#     "B-1000000MOG_USDT",
#     "B-WLFI_USDT",
#     "B-MANA_USDT",
#     "B-GALA_USDT",
#     "B-AR_USDT",
#     "B-HIPPO_USDT",
#     "B-LPT_USDT",
#     "B-AKT_USDT",
#     "B-THE_USDT",
#     "B-MANTA_USDT",
#     "B-JASMY_USDT",
#     "B-KAIA_USDT",
#     "B-AERO_USDT",
#     "B-SPX_USDT",
#     "B-SPELL_USDT",
#     "B-ETC_USDT",
#     "B-PENGU_USDT",
#     "B-FET_USDT",
#     "B-LUMIA_USDT",
#     "B-TURTLE_USDT",
#     "B-USUAL_USDT",
#     "B-HOT_USDT",
#     "B-AIXBT_USDT",
#     "B-FARTCOIN_USDT",
#     "B-ORCA_USDT",
#     "B-CKB_USDT",
#     "B-HIGH_USDT",
#     "B-KMNO_USDT",
#     "B-DEXE_USDT",
#     "B-XMR_USDT",
#     "B-PHA_USDT",
#     "B-GRIFFAIN_USDT",
#     "B-SCR_USDT",
#     "B-HAEDAL_USDT",
#     "B-BIO_USDT",
#     "B-OGN_USDT",
#     "B-GMX_USDT",
#     "B-COOKIE_USDT",
#     "B-ALCH_USDT",
#     "B-SYRUP_USDT",
#     "B-S_USDT",
#     "B-1000SHIB_USDT",
#     "B-XTZ_USDT",
#     "B-PIPPIN_USDT",
#     "B-VVV_USDT",
#     "B-IOTX_USDT",
#     "B-SSV_USDT",
#     "B-TRU_USDT",
#     "B-LQTY_USDT",
#     "B-ZRX_USDT",
#     "B-ID_USDT",
#     "B-LSK_USDT",
#     "B-COMP_USDT",
#     "B-BAND_USDT",
#     "B-RDNT_USDT",
#     "B-ARPA_USDT",
#     "B-BLUR_USDT",
#     "B-ENS_USDT",
#     "B-HFT_USDT",
#     "B-YFI_USDT",
#     "B-XVS_USDT",
#     "B-STORJ_USDT",
#     "B-DUSK_USDT",
#     "B-EDU_USDT",
#     "B-UNI_USDT",
#     "B-IMX_USDT",
#     "B-API3_USDT",
#     "B-SXT_USDT",
#     "B-DOGE_USDT",
#     "B-XAI_USDT",
#     "B-A_USDT",
#     "B-A2Z_USDT",
#     "B-1000FLOKI_USDT",
#     "B-SPK_USDT",
#     "B-AXS_USDT",
#     "B-GMT_USDT",
#     "B-NMR_USDT",
#     "B-WLD_USDT",
#     "B-LRC_USDT",
#     "B-PENDLE_USDT",
#     "B-GRT_USDT",
#     "B-AGLD_USDT",
#     "B-JUP_USDT",
#     "B-BNT_USDT",
#     "B-SEI_USDT",
#     "B-ZETA_USDT",
#     "B-C98_USDT",
#     "B-CELO_USDT",
#     "B-RIF_USDT",
#     "B-CTSI_USDT",
#     "B-RONIN_USDT",
#     "B-BERA_USDT",
#     "B-C_USDT",
#     "B-MORPHO_USDT",
#     "B-TIA_USDT",
#     "B-ORDI_USDT",
#     "B-STEEM_USDT",
#     "B-MOCA_USDT",
#     "B-DYM_USDT",
#     "B-1000BONK_USDT",
#     "B-STRK_USDT",
#     "B-CGPT_USDT",
#     "B-HOOK_USDT",
#     "B-1000RATS_USDT",
#     "B-T_USDT",
#     "B-ACE_USDT",
#     "B-1INCH_USDT",
#     "B-USTC_USDT",
#     "B-ONG_USDT",
#     "B-PIXEL_USDT",
#     "B-NKN_USDT",
#     "B-GLM_USDT",
#     "B-BSV_USDT",
#     "B-AXL_USDT",
#     "B-METIS_USDT",
#     "B-AEVO_USDT",
#     "B-ATA_USDT",
#     "B-BB_USDT",
#     "B-HBAR_USDT",
#     "B-DENT_USDT",
#     "B-FLUX_USDT",
#     "B-RPL_USDT",
#     "B-1000LUNC_USDT",
#     "B-COS_USDT",
#     "B-GOAT_USDT",
#     "B-FXS_USDT",
#     "B-PEOPLE_USDT",
#     "B-GRASS_USDT",
#     "B-MMT_USDT",
#     "B-ONDO_USDT",
#     "B-PNUT_USDT",
#     "B-SCRT_USDT",
#     "B-DOT_USDT",
#     "B-CYBER_USDT",
#     "B-ARK_USDT",
#     "B-ICX_USDT",
#     "B-OM_USDT",
#     "B-JOE_USDT",
#     "B-TWT_USDT",
#     "B-AAVE_USDT",
#     "B-PORTAL_USDT",
#     "B-ILV_USDT",
#     "B-NTRN_USDT",
#     "B-KAS_USDT",
#     "B-MAGIC_USDT",
#     "B-ACX_USDT",
#     "B-MINA_USDT",
#     "B-ASTR_USDT",
#     "B-PHB_USDT",
#     "B-SFP_USDT",
#     "B-1000PEPE_USDT",
#     "B-NOT_USDT",
#     "B-IO_USDT",
#     "B-ZK_USDT",
#     "B-KOMA_USDT",
#     "B-MASK_USDT",
#     "B-MEW_USDT",
#     "B-LISTA_USDT",
#     "B-AVA_USDT",
#     "B-HIVE_USDT",
#     "B-LDO_USDT",
#     "B-ZRO_USDT",
#     "B-RENDER_USDT",
#     "B-BANANA_USDT",
#     "B-UMA_USDT",
#     "B-VIRTUAL_USDT",
#     "B-SWARMS_USDT",
#     "B-YGG_USDT",
#     "B-STX_USDT",
#     "B-SOLV_USDT",
#     "B-ARC_USDT",
#     "B-RARE_USDT",
#     "B-AVAAI_USDT",
#     "B-TRUMP_USDT",
#     "B-MELANIA_USDT",
#     "B-VTHO_USDT",
#     "B-ANIME_USDT",
#     "B-POLYX_USDT",
#     "B-LAYER_USDT",
#     "B-HEI_USDT",
#     "B-B3_USDT",
#     "B-IP_USDT",
#     "B-GPS_USDT",
#     "B-SHELL_USDT",
#     "B-RED_USDT",
#     "B-VIC_USDT",
#     "B-EPIC_USDT",
#     "B-FORM_USDT",
#     "B-BROCCOLI714_USDT",
#     "B-PLUME_USDT",
#     "B-PARTI_USDT",
#     "B-WAL_USDT",
#     "B-BABY_USDT",
#     "B-KERNEL_USDT",
#     "B-WCT_USDT",
#     "B-INIT_USDT",
#     "B-JTO_USDT",
#     "B-G_USDT",
#     "B-ENA_USDT",
#     "B-RUNE_USDT",
#     "B-SYN_USDT",
#     "B-SYS_USDT",
#     "B-BRETT_USDT",
#     "B-SUN_USDT",
#     "B-HOME_USDT",
#     "B-DOGS_USDT",
#     "B-CATI_USDT",
#     "B-EIGEN_USDT",
#     "B-DEGEN_USDT",
#     "B-CHILLGUY_USDT",
#     "B-KITE_USDT",
#     "B-ALLO_USDT",
#     "B-ENSO_USDT",
#     "B-MON_USDT",
#     "B-NIL_USDT",
#     "B-SIGN_USDT",
#     "B-MIRA_USDT",
#     "B-ZBT_USDT",
#     "B-GIGGLE_USDT",
#     "B-FLOW_USDT",
#     "B-EUL_USDT",
#     "B-INJ_USDT",
#     "B-MEME_USDT",
#     "B-BOME_USDT",
#     "B-VINE_USDT",
#     "B-KAITO_USDT",
#     "B-ZEC_USDT",
#     "B-OP_USDT",
#     "B-CHESS_USDT",
#     "B-SONIC_USDT",
#     "B-CLANKER_USDT",
#     "B-IRYS_USDT"
# ]
TELEGRAM_BOT = "7294911972:AAE04qWQsPRhjZ3w2jCd3cYgtLT272L3Gxw"
TELEGRAM_CHAT_ID = "931437631"

CANDLE_ENDPOINT = "https://public.coindcx.com/market_data/candlesticks"

# ===========================================
# TELEGRAM FUNCTION
# ===========================================
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

# ===========================================
# WEEKLY OHLC (Mon-Sun) FUTURES PCODE=f
# ===========================================
def get_previous_week_ohlc(pair):
    try:
        IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
        now = datetime.datetime.now(IST)

        # *** This week's Monday @ 05:30 AM IST ***
        current_week_start = now - datetime.timedelta(days=now.weekday())
        current_week_start = current_week_start.replace(hour=5, minute=30, second=0, microsecond=0)

        # If it's earlier than weekly start, shift to correct week
        if now < current_week_start:
            current_week_start -= datetime.timedelta(days=7)

        # *** Previous week's Monday @ 05:30 AM and this week's Monday @ 05:00 AM ***
        previous_week_start = current_week_start - datetime.timedelta(days=7)
        week_end = current_week_start.replace(hour=5, minute=0, second=0)  # END at 5:00 AM

        start_ts = int(previous_week_start.timestamp())
        end_ts = int(week_end.timestamp())

        params = {
            "pair": pair,
            "from": start_ts,
            "to": end_ts,
            "resolution": "30",  # 30-minute candles (needed to match chart)
            "pcode": "f"         # Futures
        }

        resp = requests.get(CANDLE_ENDPOINT, params=params).json()

        # ---------- Error Handling ----------
        if resp.get("s") != "ok":
            print(f"❌ API Error → {pair} | Response: {resp}")
            return None

        if "data" not in resp or len(resp["data"]) < 3:
            print(f"⚠️ Not enough weekly candles found → {pair}")
            return None

        week = resp["data"]

        # -------- Build Correct Weekly OHLC --------
        highs = [float(c["high"]) for c in week]
        lows = [float(c["low"]) for c in week]

        week_open = float(week[0]["open"])      # Monday 05:30 AM open
        week_close = float(week[-1]["close"])   # Monday 05:00 AM close
        print(week_open)
        return {
            "open": week_open,
            "high": max(highs),
            "low": min(lows),
            "close": week_close
        }

    except Exception as e:
        print(f"🔥 ERROR in get_previous_week_ohlc() for {pair} → {e}")
        return None
# ===========================================
# TRADITIONAL PIVOTS P → S4 & R4
# ===========================================
def calculate_pivots(o):
    H, L, C = o["high"], o["low"], o["close"]
    P = (H + L + C) / 3
    print(P)
    print(H,L,C)
    return {
        "P": P,
        "R1": 2*P - L,  "S1": 2*P - H,
        "R2": P + (H-L),"S2": P - (H-L),
        "R3": H + 2*(P-L),"S3": L - 2*(H-P),
        "R4": H + 3*(P-L),"S4": L - 3*(H-P)
    }

# ===========================================
# LAST 30M CANDLE FUTURES
# ===========================================
def get_last_30m(pair):
    now = int(time.time())
    last_30m_start = now - (now % 1800) - 1800  # last completed 30-min candle start
    last_30m_end   = last_30m_start + 1800      # candle end

    params = {
        "pair": pair,
        "from": last_30m_start,
        "to": last_30m_end,
        "resolution": "30",
        "pcode": "f"
    }

    resp = requests.get(CANDLE_ENDPOINT, params=params).json()

    if resp.get("s") != "ok" or "data" not in resp or len(resp["data"]) == 0:
        print(f"⚠️ No finalized 30m candle → {pair}")
        return None

    c = resp["data"][-1]
    return {
        "open": float(c["open"]),
        "high": float(c["high"]),
        "low":  float(c["low"]),
        "close":float(c["close"])
    }

# ===========================================
# SIGNAL CHECK (YOUR EXACT CONDITIONS)
# ===========================================
def check_signal(pair, pivots, c):
    P = pivots["P"]
    o,h,l,cl = c["open"],c["high"],c["low"],c["close"]

    # SUPPORT CONDITION
    if o > P and l < P and cl > P:
        send_telegram(f"🟢 SUPPORT LONG SIGNAL\nPair: {pair}\nPivot: {P:.2f}")
        print(f"🟢 SUPPORT LONG SIGNAL\nPair: {pair}\nPivot: {P:.2f}")
    # RESISTANCE CONDITION
    if o < P and h > P and cl < P:
        send_telegram(f"🔴 RESISTANCE SHORT SIGNAL\nPair: {pair}\nPivot: {P:.2f}")
        print(f"🔴 RESISTANCE SHORT SIGNAL\nPair: {pair}\nPivot: {P:.2f}")
# ===========================================
# MAIN SCANNER
# ===========================================
def run_scanner():
    print("\n📊 Running Scan...")
    for pair in PAIRS:
        print(f"🔍 Checking → {pair}")
        
        week = get_previous_week_ohlc(pair)
        if not week: 
            continue
        
        pivots = calculate_pivots(week)
        candle = get_last_30m(pair)
        if not candle:
            continue
        
        check_signal(pair, pivots, candle)

    print("✅ Scan Completed\n")

# ===========================================
# AUTO LOOP (EVERY 30 MINUTES)
# ===========================================
print("🚀 Auto Scanner Started (Runs Every 30 Minutes)\n")

while True:
    try:
        run_scanner()
        print("⏳ Waiting 30 minutes for next scan...\n")
        time.sleep(60 * 30)
    except KeyboardInterrupt:
        print("🛑 Manual Stop Received")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(60)
