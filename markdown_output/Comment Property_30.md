Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Comment Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ProjectComponentRule Class](topic6198.md) : Comment Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the comment for the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Property Comment As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentRule](topic6198.md)
    Dim value As String
     
    instance.Comment = value
     
    value = instance.Comment  
  
C#|   
---|---  
      
    
    public abstract string Comment {get; set;}  
  
# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The rule is not writable.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentRule Class](topic6198.md)   
[ProjectComponentRule Members](topic6199.md)


