Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Comment Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [AliasRule Class](topic6001.md) : Comment Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the comment for the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Comment As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AliasRule](topic6001.md)
    Dim value As String
     
    instance.Comment = value
     
    value = instance.Comment  
  
C#|   
---|---  
      
    
    public string Comment {get; set;}  
  
# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The rule is not writable.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AliasRule Class](topic6001.md)   
[AliasRule Members](topic6002.md)


