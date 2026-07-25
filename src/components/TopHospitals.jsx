import React from 'react';


const hospitals = [
    { name: 'Apollo Hospitals', color: '#0369A1' },
    { name: 'Manipal Hospitals', color: '#0F766E' },
    { name: 'Fortis Healthcare', color: '#B91C1C' },
    { name: 'Narayana Health', color: '#1D4ED8' },
    { name: 'Aster DM Healthcare', color: '#7C3AED' },
    { name: 'Max Healthcare', color: '#C2410C' },
    { name: 'Medanta', color: '#0D9488' },
    { name: 'Global Hospital', color: '#1E40AF' },
];

const HospitalLogo = ({ hospital }) => (
    <div className="flex-shrink-0 mx-8 flex items-center gap-3 opacity-70 hover:opacity-100 transition-opacity duration-300">
        <div
            className="w-10 h-10 rounded-xl flex items-center justify-center text-white font-bold text-sm shadow-md"
            style={{ background: `linear-gradient(135deg, ${hospital.color}, ${hospital.color}99)` }}
        >
            {hospital.name.charAt(0)}
        </div>
        <span className="text-slate-600 font-semibold whitespace-nowrap text-sm">{hospital.name}</span>
    </div>
);

const TopHospitals = () => (
    <section className="py-20 bg-white overflow-hidden" aria-label="Partner hospitals">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div
                className="text-center mb-12"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-100">Partner Network</span>
                <h2 className="text-3xl font-bold text-slate-900">Trusted By Top Hospitals</h2>
                <p className="text-slate-500 mt-2">Join 8,500+ leading healthcare institutions</p>
            </div>

            <div className="relative">
                {/* Gradient fade edges */}
                <div className="absolute left-0 top-0 bottom-0 w-24 bg-gradient-to-r from-white to-transparent z-10" aria-hidden="true" />
                <div className="absolute right-0 top-0 bottom-0 w-24 bg-gradient-to-l from-white to-transparent z-10" aria-hidden="true" />

                {/* Scrolling track */}
                <div className="flex overflow-hidden py-4">
                    <div className="marquee-inner flex items-center">
                        {[...hospitals, ...hospitals].map((h, i) => (
                            <HospitalLogo key={`${h.name}-${i}`} hospital={h} />
                        ))}
                    </div>
                </div>
            </div>
        </div>
    </section>
);

export default TopHospitals;
