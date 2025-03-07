Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AssertNotDeleted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Condition Class](topic10804.md) : AssertNotDeleted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) if the item has been deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub AssertNotDeleted()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Condition](topic10804.md)
     
    instance.AssertNotDeleted()  
  
C#|   
---|---  
      
    
    protected void AssertNotDeleted()  
  
# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemDeletedException](topic3549.md)| The item has been deleted.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Condition Class](topic10804.md)   
[Condition Members](topic10805.md)


