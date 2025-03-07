Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanUndo Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ITransactionManager Interface](topic502.md) : CanUndo Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a value indicating whether there are any transactions in the undo chain. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property CanUndo As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITransactionManager](topic502.md)
    Dim value As Boolean
     
    value = instance.CanUndo  
  
C#|   
---|---  
      
    
    bool CanUndo {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)


