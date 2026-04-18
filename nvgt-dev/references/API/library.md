class library {
	library();
	bool load(const string&in filename);
	bool unload();
	bool get_active() const property;
	dictionary@ call(const string&in signature, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null, ?&in = null);
}
