import React from 'react';


const EmployerSection = () => (
    <section id="employers" className="py-24 px-4 sm:px-6 lg:px-8 bg-white relative overflow-hidden" aria-label="For employers">
        {/* Background accent */}
        <div className="absolute right-0 top-0 w-1/2 h-full bg-gradient-to-bl from-sky-50 to-transparent" aria-hidden="true" />

        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center relative z-10">
            {/* Dashboard Illustration */}
            <div
                className="relative order-2 lg:order-1"
            >
                <div className="rounded-3xl bg-gradient-to-br from-slate-900 to-slate-800 p-6 shadow-2xl shadow-slate-200">
                    {/* Window chrome */}
                    <div className="flex items-center gap-2 mb-4">
                        <div className="w-3 h-3 rounded-full bg-red-400"></div>
                        <div className="w-3 h-3 rounded-full bg-yellow-400"></div>
                        <div className="w-3 h-3 rounded-full bg-green-400"></div>
                        <div className="flex-1 h-6 rounded-full bg-slate-700 ml-2"></div>
                    </div>

                    {/* Dashboard Header */}
                    <div className="bg-slate-800 rounded-2xl p-4 mb-4">
                        <div className="text-white font-bold text-sm mb-1">Hospital Dashboard</div>
                        <div className="text-slate-400 text-xs">Apollo Hospitals · Mumbai</div>
                    </div>

                    {/* Metrics Row */}
                    <div className="grid grid-cols-3 gap-3 mb-4">
                        {[
                            { label: 'Applications', value: '248', change: '+12%', color: '#0EA5E9' },
                            { label: 'Interviews', value: '56', change: '+8%', color: '#14B8A6' },
                            { label: 'Hired', value: '18', change: '+22%', color: '#22C55E' },
                        ].map((m) => (
                            <div key={m.label} className="bg-slate-700 rounded-xl p-3">
                                <div className="text-xl font-bold text-white">{m.value}</div>
                                <div className="text-xs text-slate-400">{m.label}</div>
                                <div className="text-xs font-semibold mt-1" style={{ color: m.color }}>{m.change}</div>
                            </div>
                        ))}
                    </div>

                    {/* Pipeline */}
                    <div className="bg-slate-800 rounded-xl p-4 mb-3">
                        <div className="text-xs text-slate-400 mb-3 font-medium">Hiring Pipeline</div>
                        <div className="space-y-2">
                            {[
                                { stage: 'AI Screening', count: 180, pct: 85, color: '#0EA5E9' },
                                { stage: 'Credential Check', count: 120, pct: 60, color: '#14B8A6' },
                                { stage: 'Interview', count: 56, pct: 35, color: '#6366F1' },
                                { stage: 'Offer Sent', count: 22, pct: 15, color: '#22C55E' },
                            ].map((s) => (
                                <div key={s.stage}>
                                    <div className="flex justify-between text-xs mb-1">
                                        <span className="text-slate-300">{s.stage}</span>
                                        <span className="text-white font-semibold">{s.count}</span>
                                    </div>
                                    <div className="h-1.5 bg-slate-700 rounded-full">
                                        <div className="h-1.5 rounded-full transition-all duration-1000" style={{ width: `${s.pct}%`, background: s.color }} />
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Info bar */}
                    <div className="flex items-center gap-2 bg-sky-500/20 rounded-xl p-3 border border-sky-500/30">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                            <circle cx="12" cy="12" r="10" stroke="#0EA5E9" strokeWidth="2" />
                            <path d="M12 8v4M12 16h.01" stroke="#0EA5E9" strokeWidth="2" strokeLinecap="round" />
                        </svg>
                        <span className="text-sky-300 text-xs">3 new verified candidates ready for interview</span>
                    </div>
                </div>

                {/* Floating stats badge */}
                <div className="float absolute -bottom-6 -right-6 glass rounded-2xl p-4 shadow-xl">
                    <div className="text-2xl font-extrabold text-sky-600">40%</div>
                    <div className="text-xs text-slate-500 font-medium">Faster Hiring</div>
                </div>
            </div>

            {/* Content */}
            <div
                className="space-y-8 order-1 lg:order-2"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest border border-sky-100">For Hospitals</span>

                <h2 className="text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
                    Hire Verified<br />
                    <span className="gradient-text">Healthcare Talent</span><br />
                    with AI Screening
                </h2>

                <p className="text-lg text-slate-500 leading-relaxed">
                    Post jobs and let our AI screen, verify, and rank candidates. Access 50,000+ pre-verified healthcare professionals with proven clinical skills.
                </p>

                <div className="space-y-4">
                    {[
                        'AI-powered applicant screening & ranking',
                        'Instant license and credential verification',
                        'EMR competency test integration',
                        'Compliance & background checks',
                        'Analytics dashboard & hiring insights',
                    ].map((item) => (
                        <div key={item} className="flex items-center gap-3">
                            <div className="w-6 h-6 rounded-full bg-gradient-to-br from-sky-500 to-teal-400 flex items-center justify-center flex-shrink-0">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <path d="M5 13l4 4L19 7" stroke="white" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
                                </svg>
                            </div>
                            <span className="text-slate-700 font-medium text-sm">{item}</span>
                        </div>
                    ))}
                </div>

                <a
                    href="#"
                    className="btn-ripple inline-flex items-center gap-2 px-8 py-4 text-white font-bold rounded-2xl bg-gradient-to-r from-sky-500 to-teal-500 hover:shadow-xl hover:shadow-sky-200 hover:-translate-y-1 transition-all duration-300"
                >
                    Post a Job
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                </a>
            </div>
        </div>
    </section>
);

export default EmployerSection;
