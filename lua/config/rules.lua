
-- ─── Layer Rules ─────────────────────────────────────────────────────────────
hl.layer_rule({ match = { namespace = "^(volume_osd)$"     }, no_anim = true })
hl.layer_rule({ match = { namespace = "^(brightness_osd)$" }, no_anim = true })
hl.layer_rule({ match = { namespace = "hyprpicker"         }, no_anim = true })
hl.layer_rule({ match = { namespace = "qsdock"             }, no_anim = true })
hl.layer_rule({ match = { namespace = "qs-screenshot-overlay" }, no_anim = true })
hl.layer_rule({ match = { namespace = "ext-session-lock"   }, blur = true, ignore_alpha = 0.2 })
hl.layer_rule({ match = { namespace = "quickshell:overview%-blur" }, blur = true, ignore_alpha = 0.2 })

-- ─── Window Rules ────────────────────────────────────────────────────────────
hl.window_rule({
    match     = { title = "^(app-launcher)$" },
    float     = true,
    center    = true,
    size      = "1200 600",
    animation = "slide",
})

hl.window_rule({
    match            = { title = "^(qs-master)$" },
    float            = true,
    no_shadow        = true,
    no_initial_focus = true,
})
