Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddFailMessage Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : AddFailMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The exception message to add to the list.

Glossary Item Box

Add a failure to the [FailureMessages](topic5138.md) list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddFailMessage( _
       ByVal _message_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim message As String
     
    instance.AddFailMessage(message)  
  
C#|   
---|---  
      
    
    public void AddFailMessage( 
       string _message_
    )  
  
#### Parameters

 _message_
    The exception message to add to the list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)


