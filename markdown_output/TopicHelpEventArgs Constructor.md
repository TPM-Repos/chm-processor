       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TopicHelpEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1107.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [TopicHelpEventArgs Class](topic1101.md) : TopicHelpEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_mousePos_
    The mouse position.

_topicName_
    The name of the topic to show.

Glossary Item Box

Initializes a new instance of the [TopicHelpEventArgs](topic1101.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _mousePos_ As Point, _
       ByVal _topicName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim mousePos As Point
    Dim topicName As String
     
    Dim instance As New [TopicHelpEventArgs](topic1101.md)(mousePos, topicName)  
  
C#|   
---|---  
      
    
    public TopicHelpEventArgs( 
       Point _mousePos_ ,
       string _topicName_
    )  
  
#### Parameters

 _mousePos_
    The mouse position.
_topicName_
    The name of the topic to show.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TopicHelpEventArgs Class](topic1101.md)   
[TopicHelpEventArgs Members](topic1102.md)

©2024 DriveWorks Ltd. All Rights Reserved.
