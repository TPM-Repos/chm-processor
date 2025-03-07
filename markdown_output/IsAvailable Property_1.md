Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsAvailable Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommand Interface](topic77.md) : IsAvailable Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether the command is available. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property IsAvailable As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommand](topic77.md)
    Dim value As Boolean
     
    value = instance.IsAvailable  
  
C#|   
---|---  
      
    
    bool IsAvailable {get;}  
  
# Remarks

If either the [IsEnabled](topic88.md) or the [IsValid](topic89.md) is false, the command is unavailable, i.e. it cannot be invoked, otherwise it is true.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommand Interface](topic77.md)   
[ICommand Members](topic78.md)


