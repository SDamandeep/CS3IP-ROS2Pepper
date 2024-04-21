module PepperMove {
    interface Movement {
        void moveForward();
        void mMove(float forward, float sideways, float angular);
        void returnImage();
        void moveLeftArm(float lspitch, float lsroll, float lelbowyaw, float lelbowroll);
        void moveRightArm(float lspitch, float lsroll, float lelbowyaw, float lelbowroll);
    };
};
