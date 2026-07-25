import React, { useEffect, useRef, useState } from 'react';


const stats = [
    {
        value: 15000, suffix: '+', label: 'Active Jobs', icon: (
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <rect x="2" y="7" width="20" height="14" rx="2" stroke="white" strokeWidth="2" />
                <path d="M16 7V5C16 3.89543 15.1046 3 14 3H10C8.89543 3 8 3.89543 8 5V7" stroke="white" strokeWidth="2" />
            </svg>
        ), gradient: 'from-sky-500 to-cyan-400', bg: 'from-sky-50 to-cyan-50', border: 'border-sky-100'
    },
    {
        value: 8500, suffix: '+', label: 'Hospitals', icon: (
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <path d="M3 9L12 2L21 9V20C21 20.5523 20.5523 21 20 21H4C3.44772 21 3 20.5523 3 20V9Z" stroke="white" strokeWidth="2" />
                <path d="M12 5L12 19M7 12L17 12" stroke="white" strokeWidth="2" strokeLinecap="round" />
            </svg>
        ), gradient: 'from-teal-500 to-emerald-400', bg: 'from-teal-50 to-emerald-50', border: 'border-teal-100'
    },
    {
        value: 25000, suffix: '+', label: 'Professionals', icon: (
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <circle cx="8" cy="7" r="3" stroke="white" strokeWidth="2" />
                <circle cx="16" cy="7" r="3" stroke="white" strokeWidth="2" />
                <path d="M2 21C2 17.134 4.68629 14 8 14H16C19.3137 14 22 17.134 22 21" stroke="white" strokeWidth="2" strokeLinecap="round" />
            </svg>
        ), gradient: 'from-indigo-500 to-purple-500', bg: 'from-indigo-50 to-purple-50', border: 'border-indigo-100'
    },
    {
        value: 100, suffix: '%', label: 'Verified Jobs', icon: (
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
        ), gradient: 'from-green-500 to-emerald-400', bg: 'from-green-50 to-emerald-50', border: 'border-green-100'
    },
    {
        value: 50, suffix: '+', label: 'Cities', icon: (
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="white" />
            </svg>
        ), gradient: 'from-orange-500 to-amber-400', bg: 'from-orange-50 to-amber-50', border: 'border-orange-100'
    },
];

const useCountUp = (end, duration = 2000, shouldStart = false) => {
    const [count, setCount] = useState(0);
    useEffect(() => {
        if (!shouldStart) return;
        let start = 0;
        const step = end / (duration / 16);
        const timer = setInterval(() => {
            start += step;
            if (start >= end) { setCount(end); clearInterval(timer); }
            else setCount(Math.floor(start));
        }, 16);
        return () => clearInterval(timer);
    }, [end, duration, shouldStart]);
    return count;
};

const StatCard = ({ stat, index }) => {
    const [inView, setInView] = useState(false);
    const ref = useRef(null);
    const count = useCountUp(stat.value, 2000, inView);

    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) setInView(true);
        }, { threshold: 0.5 });
        if (ref.current) observer.observe(ref.current);
        return () => observer.disconnect();
    }, []);

    return (
        <div
            ref={ref}
            className={`hover-lift relative overflow-hidden rounded-2xl border ${stat.border} bg-gradient-to-br ${stat.bg} p-6 shadow-lg`}
        >
            {/* Glow circle */}
            <div className={`absolute -top-6 -right-6 w-24 h-24 rounded-full bg-gradient-to-br ${stat.gradient} opacity-15 blur-2xl`} aria-hidden="true" />

            <div className={`w-14 h-14 rounded-2xl bg-gradient-to-br ${stat.gradient} flex items-center justify-center mb-4 shadow-lg`}>
                {stat.icon}
            </div>
            <div className="text-4xl font-extrabold text-slate-900 leading-none">
                {count.toLocaleString()}<span className="text-sky-500">{stat.suffix}</span>
            </div>
            <div className="text-slate-500 font-medium mt-1 text-sm">{stat.label}</div>
        </div>
    );
};

const Statistics = () => (
    <section className="py-20 px-4 sm:px-6 lg:px-8 bg-white" aria-label="Platform statistics">
        <div className="max-w-7xl mx-auto">
            <div
                className="text-center mb-14"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-100">By The Numbers</span>
                <h2 className="text-4xl font-bold text-slate-900">Trusted By Thousands</h2>
                <p className="text-slate-500 mt-3 max-w-lg mx-auto">The largest healthcare recruitment network in India</p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-5">
                {stats.map((stat, i) => <StatCard key={stat.label} stat={stat} index={i} />)}
            </div>
        </div>
    </section>
);

export default Statistics;
