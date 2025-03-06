       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StatusMessageEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [StatusMessageEventArgs Class](topic9981.md) : StatusMessageEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message for this status event.

_isError_
    Whether or not this message is an error.

Glossary Item Box

Creates a new instance of the [StatusMessageEventArgs](topic9981.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _isError_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As String
    Dim isError As Boolean
     
    Dim instance As New [StatusMessageEventArgs](topic9981.md)(message, isError)  
  
C#|   
---|---  
      
    
    public StatusMessageEventArgs( 
       string _message_ ,
       bool _isError_
    )  
  
#### Parameters

 _message_
    The message for this status event.
_isError_
    Whether or not this message is an error.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StatusMessageEventArgs Class](topic9981.md)   
[StatusMessageEventArgs Members](topic9982.md)


