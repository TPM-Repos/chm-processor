Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Recipients Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : Recipients Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the email addresses that the email should be sent to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Recipients As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim value() As String
     
    instance.Recipients = value
     
    value = instance.Recipients  
  
C#|   
---|---  
      
    
    public string[] Recipients {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)


