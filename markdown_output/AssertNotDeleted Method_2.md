Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AssertNotDeleted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : AssertNotDeleted Method  
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
      
    
    Dim instance As [Task](topic11629.md)
     
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

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


