Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PromptAndApplyChangesResult Enumeration   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : PromptAndApplyChangesResult Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Stores the result of a call to TryPromptAndApplyChanges of IPendingChangesService. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum PromptAndApplyChangesResult 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PromptAndApplyChangesResult](topic660.md)  
  
C#|   
---|---  
      
    
    public enum PromptAndApplyChangesResult : System.Enum   
  
# Members

Member| Description  
---|---  
**Cancel**|  The process has been canceled.  
**No**|  The changes were not applied.  
**NoChanges**|  No changes have been made to the project and so the user was never prompted.  
**Yes**|  The changes were applied.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Applications.PromptAndApplyChangesResult**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Applications Namespace](topic16.md)


