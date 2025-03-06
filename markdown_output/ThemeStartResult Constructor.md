       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ThemeStartResult Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ThemeStartResult Class](topic1092.md) : ThemeStartResult Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_started_
    A boolean representing whether the theme started successfully.

_failureReason_
    An optional description of the problem if the theme failed to start.

Glossary Item Box

Creates a new instance of the [ThemeStartResult](topic1092.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _started_ As Boolean, _
       Optional ByVal _failureReason_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim started As Boolean
    Dim failureReason As String
     
    Dim instance As New [ThemeStartResult](topic1092.md)(started, failureReason)  
  
C#|   
---|---  
      
    
    public ThemeStartResult( 
       bool _started_ ,
       string _failureReason_
    )  
  
#### Parameters

 _started_
    A boolean representing whether the theme started successfully.
_failureReason_
    An optional description of the problem if the theme failed to start.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ThemeStartResult Class](topic1092.md)   
[ThemeStartResult Members](topic1093.md)


