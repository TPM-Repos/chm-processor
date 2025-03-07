Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddFailure Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : AddFailure Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reason_
    The reason the email failed to be sent.

Glossary Item Box

Logs a failed attempt at sending this email. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddFailure( _
       ByVal _reason_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim reason As String
     
    instance.AddFailure(reason)  
  
C#|   
---|---  
      
    
    public void AddFailure( 
       string _reason_
    )  
  
#### Parameters

 _reason_
    The reason the email failed to be sent.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)


