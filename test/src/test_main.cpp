#include <gtest/gtest.h>

// Example function to test
int add(int a, int b) {
    return a + b;
}

// Test case
TEST(AdditionTest, BasicAssertions) {
    EXPECT_EQ(add(1, 1), 2);
    EXPECT_EQ(add(2, 2), 4);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

