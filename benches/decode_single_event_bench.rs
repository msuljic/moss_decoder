use criterion::Criterion;

const BENCH_FILE_PATH: &str = "tests/test-data/moss_noise.raw";

pub fn decode_single_event(c: &mut Criterion) {
    let f = std::fs::read(std::path::PathBuf::from(BENCH_FILE_PATH)).unwrap();

    let mut group = c.benchmark_group("decode single event");
    {
        group.bench_function("decode event fsm iterator", |b| {
            b.iter(|| moss_decoder::decode_event(&f))
        });
    }
    group.finish();
}
