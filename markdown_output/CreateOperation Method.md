Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : CreateOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The unique name of the operation.

Glossary Item Box

Creates and returns a new operation with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateOperation( _
       ByVal _name_ As String _
    ) As [Operation](topic11068.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim name As String
    Dim value As [Operation](topic11068.md)
     
    value = instance.CreateOperation(name)  
  
C#|   
---|---  
      
    
    public [Operation](topic11068.md) CreateOperation( 
       string _name_
    )  
  
#### Parameters

 _name_
    The unique name of the operation.

# Remarks

Multiple operations can share the same title and been hidden/shown based on conditions to allow operations which are conceptually similar but with different semantics based on the environment state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


