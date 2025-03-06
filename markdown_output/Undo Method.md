       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Undo Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic511.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ITransactionManager Interface](topic502.md) : Undo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Undoes the last transaction in the undo chain. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function Undo() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITransactionManager](topic502.md)
    Dim value As Boolean
     
    value = instance.Undo()  
  
C#|   
---|---  
      
    
    bool Undo()  
  
#### Return Value

True if there was a transaction in the undo chain, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)

©2024 DriveWorks Ltd. All Rights Reserved.
