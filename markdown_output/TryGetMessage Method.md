       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetMessage Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4641.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : TryGetMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_code_
    The code of the message to retrieve.

_message_
    A reference to a variable which will receive the message.

Glossary Item Box

Gets the message with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function TryGetMessage( _
       ByVal _code_ As Integer, _
       ByRef _message_ As [ProjectMessage](topic4601.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim code As Integer
    Dim message As [ProjectMessage](topic4601.md)
    Dim value As Boolean
     
    value = instance.TryGetMessage(code, message)  
  
C#|   
---|---  
      
    
    public abstract bool TryGetMessage( 
       int _code_ ,
       ref [ProjectMessage](topic4601.md) _message_
    )  
  
#### Parameters

 _code_
    The code of the message to retrieve.
_message_
    A reference to a variable which will receive the message.

#### Return Value

True if the message is found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)

©2024 DriveWorks Ltd. All Rights Reserved.
