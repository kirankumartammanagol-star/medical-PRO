import React from 'react';
import { motion } from 'framer-motion';

const fadeUp = {
    hidden: { opacity: 0, y: 30 },
    visible: (i = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.15, duration: 0.7, ease: 'easeOut' } }),
};

const FloatingCard = ({ children, className, delay = 0 }) => (
    <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay, duration: 0.6, ease: 'easeOut' }}
        className={`glass rounded-2xl shadow-xl shadow-sky-100/40 ${className}`}
        style={{ animation: `float ${3.5 + delay}s ease-in-out ${delay}s infinite` }}
    >
        {children}
    </motion.div>
);

const Hero = () => {
    return (
        <section
            id="home"
            className="relative min-h-screen flex items-center overflow-hidden pt-24 pb-12"
            aria-label="Hero section"
        >
            {/* Background Blobs */}
            <div className="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
                <div className="blob absolute -top-40 -left-40 w-[600px] h-[600px] bg-gradient-to-br from-sky-200/60 to-teal-200/40 rounded-full blur-3xl" />
                <div className="blob absolute top-1/2 -right-40 w-[500px] h-[500px] bg-gradient-to-br from-indigo-200/50 to-purple-200/40 rounded-full blur-3xl" style={{ animationDelay: '2s' }} />
                <div className="blob absolute bottom-0 left-1/3 w-[400px] h-[400px] bg-gradient-to-br from-teal-200/40 to-sky-200/30 rounded-full blur-3xl" style={{ animationDelay: '4s' }} />
                {/* Floating Icon Badges */}
                <div className="float absolute top-36 right-[28%] w-11 h-11 rounded-2xl bg-white/90 shadow-lg flex items-center justify-center hidden lg:flex">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 2L12 22M2 12L22 12" stroke="#0EA5E9" strokeWidth="2.5" strokeLinecap="round" /></svg>
                </div>
                <div className="float-delay-1 absolute bottom-36 right-[8%] w-10 h-10 rounded-xl bg-white/90 shadow-lg items-center justify-center hidden lg:flex">
                    <svg width="20" height="20" viewBox="0 0 24 24"><path d="M12 21.593C-4.667 11.538 4.2 0 12 0c7.8 0 16.667 11.538 0 21.593z" fill="#EF4444" /></svg>
                </div>
                <div className="float-delay-2 absolute top-52 left-[5%] w-10 h-10 rounded-xl bg-white/90 shadow-lg items-center justify-center hidden lg:flex">
                    <svg width="20" height="20" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z" fill="#14B8A6" /></svg>
                </div>
            </div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <div className="grid lg:grid-cols-2 gap-12 xl:gap-16 items-center">

                    {/* ── Left Content ── */}
                    <div className="flex flex-col items-start gap-7">

                        {/* Badge */}
                        <motion.div
                            variants={fadeUp} initial="hidden" animate="visible" custom={0}
                            className="inline-flex items-center gap-2 glass rounded-full px-4 py-2 text-sm font-medium text-sky-600 border border-sky-100"
                        >
                            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" aria-hidden="true" />
                            Trusted by 150+ Hospitals across India
                        </motion.div>

                        {/* Heading */}
                        <motion.h1
                            variants={fadeUp} initial="hidden" animate="visible" custom={1}
                            className="text-5xl sm:text-6xl lg:text-6xl xl:text-7xl font-bold leading-[1.1] text-slate-900"
                        >
                            Find Your Dream{' '}
                            <span className="gradient-text">Healthcare Career</span>
                        </motion.h1>

                        {/* Subtitle */}
                        <motion.p
                            variants={fadeUp} initial="hidden" animate="visible" custom={2}
                            className="text-lg text-slate-500 max-w-lg leading-relaxed"
                        >
                            Connecting healthcare professionals with verified hospitals through AI-powered recruitment,
                            credential verification, EMR competency testing, and career analytics.
                        </motion.p>

                        {/* CTA Buttons */}
                        <motion.div
                            variants={fadeUp} initial="hidden" animate="visible" custom={3}
                            className="flex flex-wrap items-center gap-4"
                        >
                            <a
                                href="#jobs"
                                className="btn-ripple inline-flex items-center gap-2 px-7 py-3.5 text-white font-semibold rounded-2xl bg-gradient-to-r from-sky-500 to-teal-500 hover:shadow-xl hover:shadow-sky-200 hover:-translate-y-1 transition-all duration-300 text-sm"
                            >
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <circle cx="11" cy="11" r="8" stroke="white" strokeWidth="2.2" />
                                    <path d="M21 21l-4.35-4.35" stroke="white" strokeWidth="2.2" strokeLinecap="round" />
                                </svg>
                                Search Jobs
                            </a>
                            <a
                                href="#features"
                                className="btn-ripple inline-flex items-center gap-2 px-7 py-3.5 text-slate-700 font-semibold rounded-2xl bg-white hover:bg-slate-50 border border-slate-200 hover:border-sky-300 hover:-translate-y-1 transition-all duration-300 shadow-md text-sm"
                            >
                                Explore Features
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <path d="M5 12h14M12 5l7 7-7 7" stroke="#0EA5E9" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                </svg>
                            </a>
                        </motion.div>

                        {/* Social Proof */}
                        <motion.div
                            variants={fadeUp} initial="hidden" animate="visible" custom={4}
                            className="flex flex-wrap items-center gap-5"
                        >
                            {/* Avatars */}
                            <div className="flex items-center gap-3">
                                <div className="flex -space-x-2.5">
                                    {['#0EA5E9', '#14B8A6', '#6366F1', '#22C55E', '#F59E0B'].map((c, i) => (
                                        <div
                                            key={i}
                                            className="w-9 h-9 rounded-full border-2 border-white flex items-center justify-center text-white text-xs font-bold shadow"
                                            style={{ background: c }}
                                            aria-hidden="true"
                                        >
                                            {['D', 'N', 'S', 'P', 'R'][i]}
                                        </div>
                                    ))}
                                </div>
                                <div>
                                    <div className="font-bold text-slate-900 text-sm">50,000+</div>
                                    <div className="text-slate-500 text-xs">Healthcare Professionals</div>
                                </div>
                            </div>

                            <div className="h-10 w-px bg-slate-200" aria-hidden="true" />

                            {/* Stars */}
                            <div>
                                <div className="font-bold text-slate-900 text-sm">150+ Hospitals</div>
                                <div className="flex items-center gap-0.5 mt-1">
                                    {[...Array(5)].map((_, i) => (
                                        <svg key={i} width="13" height="13" viewBox="0 0 24 24" fill="#F59E0B" aria-hidden="true">
                                            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                                        </svg>
                                    ))}
                                </div>
                            </div>
                        </motion.div>
                    </div>

                    {/* ── Right Side – Illustration ── */}
                    <motion.div
                        initial={{ opacity: 0, x: 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.9, ease: 'easeOut', delay: 0.3 }}
                        className="relative hidden lg:flex items-center justify-center"
                    >
                        <div className="relative w-full max-w-md xl:max-w-lg aspect-square">
                            {/* Background  */}
                            <div className="absolute inset-0 rounded-[40px] bg-gradient-to-br from-sky-100 to-teal-50 shadow-2xl shadow-sky-100" />

                            {/* SVG Illustration */}
                            <div className="absolute inset-4 rounded-[32px] overflow-hidden bg-gradient-to-br from-sky-50 to-white flex items-center justify-center">
                                <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full p-6">
                                    <circle cx="200" cy="200" r="180" fill="url(#bgGrad)" opacity="0.3" />
                                    <defs>
                                        <radialGradient id="bgGrad" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stopColor="#0EA5E9" stopOpacity="0.2" />
                                            <stop offset="100%" stopColor="#14B8A6" stopOpacity="0.05" />
                                        </radialGradient>
                                        <linearGradient id="skinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" stopColor="#FBBF24" />
                                            <stop offset="100%" stopColor="#F59E0B" />
                                        </linearGradient>
                                        <linearGradient id="coatGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" stopColor="#ffffff" />
                                            <stop offset="100%" stopColor="#E2E8F0" />
                                        </linearGradient>
                                        <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" stopColor="#0EA5E9" />
                                            <stop offset="100%" stopColor="#0284C7" />
                                        </linearGradient>
                                        <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" stopColor="#14B8A6" />
                                            <stop offset="100%" stopColor="#0D9488" />
                                        </linearGradient>
                                    </defs>
                                    {/* Doctor Center */}
                                    <rect x="155" y="230" width="90" height="120" rx="20" fill="url(#coatGrad)" stroke="#CBD5E1" strokeWidth="1.5" />
                                    <rect x="160" y="260" width="80" height="90" rx="10" fill="url(#blueGrad)" />
                                    <path d="M185 245 Q190 280 200 285 Q220 290 225 270 Q230 255 225 245" stroke="#1E293B" strokeWidth="3" fill="none" strokeLinecap="round" />
                                    <circle cx="200" cy="285" r="8" fill="#1E293B" />
                                    <ellipse cx="200" cy="200" rx="32" ry="36" fill="url(#skinGrad)" />
                                    <ellipse cx="200" cy="178" rx="32" ry="18" fill="#1E293B" />
                                    <ellipse cx="200" cy="166" rx="16" ry="12" fill="#374151" />
                                    <ellipse cx="190" cy="198" rx="4" ry="5" fill="white" />
                                    <ellipse cx="210" cy="198" rx="4" ry="5" fill="white" />
                                    <circle cx="191" cy="199" r="2.5" fill="#1E293B" />
                                    <circle cx="211" cy="199" r="2.5" fill="#1E293B" />
                                    <path d="M192 210 Q200 217 208 210" stroke="#92400E" strokeWidth="2" fill="none" strokeLinecap="round" />
                                    <path d="M175 230 L200 245 L225 230" fill="#E2E8F0" stroke="#CBD5E1" strokeWidth="1" />
                                    <rect x="188" y="260" width="24" height="32" rx="4" fill="#0EA5E9" />
                                    <rect x="192" y="267" width="16" height="4" rx="2" fill="white" opacity="0.8" />
                                    <rect x="192" y="275" width="12" height="3" rx="1.5" fill="white" opacity="0.6" />
                                    {/* Nurse Left */}
                                    <rect x="65" y="250" width="75" height="110" rx="18" fill="url(#tealGrad)" />
                                    <ellipse cx="102" cy="215" rx="28" ry="32" fill="#FDDCB5" />
                                    <ellipse cx="102" cy="196" rx="28" ry="16" fill="#374151" />
                                    <rect x="88" y="188" width="28" height="10" rx="5" fill="white" />
                                    <path d="M96 188 L108 188" stroke="#EF4444" strokeWidth="2" />
                                    <ellipse cx="94" cy="213" rx="3.5" ry="4" fill="white" />
                                    <ellipse cx="110" cy="213" rx="3.5" ry="4" fill="white" />
                                    <circle cx="95" cy="214" r="2" fill="#1E293B" />
                                    <circle cx="111" cy="214" r="2" fill="#1E293B" />
                                    <path d="M97 222 Q102 228 107 222" stroke="#92400E" strokeWidth="1.5" fill="none" strokeLinecap="round" />
                                    <rect x="55" y="270" width="40" height="52" rx="4" fill="#F1F5F9" stroke="#CBD5E1" strokeWidth="1.5" />
                                    <path d="M62 283 L88 283M62 292 L82 292M62 301 L85 301M62 310 L78 310" stroke="#94A3B8" strokeWidth="1.5" strokeLinecap="round" />
                                    <rect x="70" y="273" width="20" height="8" rx="2" fill="#0EA5E9" />
                                    {/* Surgeon Right */}
                                    <rect x="260" y="248" width="80" height="112" rx="18" fill="#4F46E5" />
                                    <ellipse cx="300" cy="212" rx="30" ry="34" fill="#FDDCB5" />
                                    <ellipse cx="300" cy="195" rx="30" ry="14" fill="#E2E8F0" />
                                    <rect x="275" y="214" width="50" height="20" rx="6" fill="#E2E8F0" />
                                    <ellipse cx="300" cy="192" rx="32" ry="14" fill="#0284C7" />
                                    <ellipse cx="290" cy="207" rx="4" ry="4.5" fill="white" />
                                    <ellipse cx="310" cy="207" rx="4" ry="4.5" fill="white" />
                                    <circle cx="291" cy="208" r="2.5" fill="#1E293B" />
                                    <circle cx="311" cy="208" r="2.5" fill="#1E293B" />
                                    <ellipse cx="268" cy="305" rx="18" ry="12" fill="#22C55E" opacity="0.8" />
                                    <ellipse cx="332" cy="305" rx="18" ry="12" fill="#22C55E" opacity="0.8" />
                                    {/* Cross */}
                                    <path d="M195 127 L205 127 L205 137 L215 137 L215 147 L205 147 L205 157 L195 157 L195 147 L185 147 L185 137 L195 137 Z" fill="#EF4444" />
                                    <rect x="80" y="355" width="240" height="12" rx="6" fill="#E2E8F0" opacity="0.5" />
                                </svg>
                            </div>

                            {/* Floating Cards — positioned around the box */}
                            <FloatingCard className="absolute -top-5 -left-5 flex items-center gap-3 px-4 py-3 w-44" delay={0.5}>
                                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-500 flex items-center justify-center shadow-md flex-shrink-0">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                        <path d="M9 3H15M9 3C9 3 5 4 5 9C5 14 9 15 9 15H15C15 15 19 14 19 9C19 4 15 3 15 3M9 3C9 3 9 6 12 6C15 6 15 3 15 3" stroke="white" strokeWidth="2" strokeLinecap="round" />
                                        <path d="M12 11V17M9 14H15" stroke="white" strokeWidth="2" strokeLinecap="round" />
                                    </svg>
                                </div>
                                <div>
                                    <div className="font-bold text-slate-900 text-sm leading-tight">AI Match</div>
                                    <div className="text-xs text-indigo-500 font-semibold">98% Accuracy</div>
                                </div>
                            </FloatingCard>

                            <FloatingCard className="absolute -bottom-5 -left-5 flex items-center gap-3 px-4 py-3 w-48" delay={1}>
                                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center shadow-md flex-shrink-0">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                        <path d="M9 12L11 14L15 10M21 12C21 16.97 16.97 21 12 21C7.03 21 3 16.97 3 12C3 7.03 7.03 3 12 3C16.97 3 21 7.03 21 12Z" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                                    </svg>
                                </div>
                                <div>
                                    <div className="font-bold text-slate-900 text-sm leading-tight">Credentials</div>
                                    <div className="text-xs text-green-500 font-semibold">Verified ✓</div>
                                </div>
                            </FloatingCard>

                            <FloatingCard className="absolute top-1/2 -translate-y-1/2 -right-5 flex items-center gap-3 px-4 py-3 w-44" delay={1.5}>
                                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-sky-400 to-cyan-500 flex items-center justify-center shadow-md flex-shrink-0">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                        <path d="M12 2L4 6V12C4 16.4 7.4 20.5 12 21.5C16.6 20.5 20 16.4 20 12V6L12 2Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                        <path d="M9 12L11 14L15 10" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                    </svg>
                                </div>
                                <div>
                                    <div className="font-bold text-slate-900 text-sm leading-tight">HIPAA</div>
                                    <div className="text-xs text-sky-500 font-semibold">Compliant</div>
                                </div>
                            </FloatingCard>

                            <FloatingCard className="absolute -bottom-5 right-6 flex items-center gap-3 px-4 py-3 w-40" delay={2}>
                                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-orange-400 to-red-400 flex items-center justify-center shadow-md flex-shrink-0">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                        <circle cx="12" cy="12" r="3" fill="white" />
                                        <path d="M12 2V5M12 19V22M2 12H5M19 12H22" stroke="white" strokeWidth="2" strokeLinecap="round" />
                                    </svg>
                                </div>
                                <div>
                                    <div className="font-bold text-slate-900 text-sm leading-tight">Live Jobs</div>
                                    <div className="text-xs text-orange-500 font-semibold">15,000+</div>
                                </div>
                            </FloatingCard>
                        </div>
                    </motion.div>
                </div>
            </div>
        </section>
    );
};

export default Hero;
