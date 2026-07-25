import React from 'react';


const features = [
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M9 12L11 14L15 10M21 12C21 16.97 16.97 21 12 21C7.03 21 3 16.97 3 12C3 7.03 7.03 3 12 3C16.97 3 21 7.03 21 12Z" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" /></svg>),
        gradient: 'from-sky-500 to-cyan-400',
        title: 'Credential Verification',
        desc: 'AI instantly verifies medical licenses, certifications, and NMC registrations in real-time.',
        badge: 'Real-time',
    },
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M9 3H15M9 3C9 3 5 4 5 9C5 14 9 15 9 15H15C15 15 19 14 19 9C19 4 15 3 15 3M9 3C9 3 9 6 12 6C15 6 15 3 15 3" stroke="white" strokeWidth="2" strokeLinecap="round" /><path d="M12 11V17M9 14H15" stroke="white" strokeWidth="2" strokeLinecap="round" /></svg>),
        gradient: 'from-indigo-500 to-purple-500',
        title: 'AI Matching',
        desc: 'Machine learning matches candidates to jobs based on skills, experience, and cultural fit.',
        badge: '98% Accuracy',
    },
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="2" y="3" width="20" height="14" rx="2" stroke="white" strokeWidth="2" /><path d="M8 21h8M12 17v4" stroke="white" strokeWidth="2" strokeLinecap="round" /><path d="M7 10L10 13L17 7" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" /></svg>),
        gradient: 'from-teal-500 to-emerald-400',
        title: 'Clinical Skills Assessment',
        desc: 'Evaluate ICD-10, SNOMED CT, EMR proficiency through adaptive clinical assessments.',
        badge: 'EMR Ready',
    },
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M3 3v18h18" stroke="white" strokeWidth="2" strokeLinecap="round" /><path d="M7 16L10 11L13 14L17 8" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" /></svg>),
        gradient: 'from-orange-500 to-amber-400',
        title: 'Career Analytics',
        desc: 'Real-time salary insights, career growth trajectories, and market demand forecasting.',
        badge: 'Live Data',
    },
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" /><path d="M2 17L12 22L22 17" stroke="white" strokeWidth="2" strokeLinecap="round" /><path d="M2 12L12 17L22 12" stroke="white" strokeWidth="2" strokeLinecap="round" /></svg>),
        gradient: 'from-pink-500 to-rose-400',
        title: 'Learning Portal',
        desc: 'Accredited courses, CME credits, certification prep, and compliance training programs.',
        badge: 'CME Credits',
    },
    {
        icon: (<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="3" stroke="white" strokeWidth="2" /><path d="M7 8H17M7 12H13M7 16H10" stroke="white" strokeWidth="2" strokeLinecap="round" /></svg>),
        gradient: 'from-violet-500 to-indigo-500',
        title: 'Hospital Dashboard',
        desc: 'Comprehensive recruitment analytics, hiring pipeline management, and workforce planning.',
        badge: 'Enterprise',
    },
];

const Features = () => (
    <section id="features" className="py-24 px-4 sm:px-6 lg:px-8 relative overflow-hidden" aria-label="Platform features">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-sky-900" aria-hidden="true" />
        <div className="absolute inset-0 pointer-events-none" aria-hidden="true">
            <div className="absolute top-0 left-1/4 w-96 h-96 bg-sky-500 rounded-full blur-3xl opacity-10" />
            <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-teal-500 rounded-full blur-3xl opacity-10" />
        </div>

        <div className="max-w-7xl mx-auto relative z-10">
            {/* Header */}
            <div
                className="text-center mb-16 max-w-2xl mx-auto"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-500/20 text-sky-300 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-500/30">
                    Platform Features
                </span>
                <h2 className="text-4xl sm:text-5xl font-bold text-white mb-4">
                    Why Choose <span className="gradient-text">HealthCareer Pro</span>
                </h2>
                <p className="text-slate-400 text-lg leading-relaxed">
                    Everything you need to accelerate your healthcare career or find the perfect candidate
                </p>
            </div>

            {/* Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {features.map((f, i) => (
                    <div
                        key={f.title}
                        className="group relative hover-lift rounded-2xl p-7 cursor-default flex flex-col"
                        style={{
                            background: 'rgba(255,255,255,0.04)',
                            border: '1px solid rgba(255,255,255,0.1)',
                            backdropFilter: 'blur(12px)',
                        }}
                    >
                        <div className={`absolute inset-0 rounded-2xl bg-gradient-to-br ${f.gradient} opacity-0 group-hover:opacity-10 transition-opacity duration-500`} aria-hidden="true" />

                        {/* Icon + Badge Row */}
                        <div className="flex items-center justify-between mb-5">
                            <div className={`w-13 h-13 w-14 h-14 rounded-2xl bg-gradient-to-br ${f.gradient} flex items-center justify-center shadow-lg flex-shrink-0`}>
                                {f.icon}
                            </div>
                            <span className={`px-2.5 py-1 rounded-full text-xs font-bold border border-white/10 text-white/70 bg-white/5`}>
                                {f.badge}
                            </span>
                        </div>

                        <h3 className="text-lg font-bold text-white mb-2">{f.title}</h3>
                        <p className="text-slate-400 text-sm leading-relaxed flex-1">{f.desc}</p>

                        <div className="mt-5 flex items-center gap-1.5 text-sky-400 text-sm font-semibold">
                            <span>Learn more</span>
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                <path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                            </svg>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    </section>
);

export default Features;
