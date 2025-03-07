Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MessageEventArgs Constructor(ProjectMessage)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [MessageEventArgs Class](topic3704.md) > [MessageEventArgs Constructor](topic3710.md) : MessageEventArgs Constructor(ProjectMessage)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message that was changed.

Glossary Item Box

Initializes a new instance of the [MessageEventArgs](topic3704.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As [ProjectMessage](topic4601.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As [ProjectMessage](topic4601.md)
     
    Dim instance As New [MessageEventArgs](topic3704.md)(message)  
  
C#|   
---|---  
      
    
    public MessageEventArgs( 
       [ProjectMessage](topic4601.md) _message_
    )  
  
#### Parameters

 _message_
    The message that was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[MessageEventArgs Class](topic3704.md)   
[MessageEventArgs Members](topic3705.md)   
[Overload List](topic3710.md)


