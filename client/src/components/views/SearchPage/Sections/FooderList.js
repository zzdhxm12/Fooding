import React, { useState } from 'react';
import { Row, Col, Avatar } from 'antd';
import { UserOutlined, CloseCircleOutlined } from '@ant-design/icons';

function FooderList(props) {
  const renderFollowList = () =>
    props.followingList.map((follow, index) => (
      <Row style={{ margin: '1rem 2.5rem' }} key={index}>
        <Col>
          <Avatar size="large" icon={<UserOutlined />} />
        </Col>
        <Col
          span={18}
          style={{ display: 'flex', alignItems: 'center', marginLeft: '1rem' }}
        >
          {follow.nickname}
        </Col>
        <Col style={{ display: 'flex', alignItems: 'center' }}>
          <CloseCircleOutlined style={{ fontSize: '20px' }} />
        </Col>
      </Row>
    ));
  return (
    <>
      <>{renderFollowList()}</>
    </>
  );
}

export default FooderList;
