package com.project6.gilhari;

import org.json.JSONException;
import org.json.JSONObject;
import com.softwaretree.jdx.JDX_JSONObject;

public class Allotted extends JDX_JSONObject {
    public Student student;
    public Course course;

    public Allotted() {
        super();
    }

    public Allotted(JSONObject jsonObject) throws JSONException {
        super(jsonObject);
    }
}
