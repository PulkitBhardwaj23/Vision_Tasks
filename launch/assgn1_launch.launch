<launch>
    <!-- Launch the talker node with specified parameters -->
    <node name="talker_node" pkg="assgn1" type="talker.py" output="screen">
        <rosparam command="load" file="$(find assgn1)/launch/parameters.yaml" />
    </node>

    <!-- Launch the relay node -->
    <node name="relay_node" pkg="assgn1" type="relay.py" output="screen"/>

</launch>
