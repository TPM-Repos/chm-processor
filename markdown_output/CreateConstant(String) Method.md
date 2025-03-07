Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateConstant(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) > [CreateConstant Method](topic4252.md) : CreateConstant(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name to assign to the constant.

Glossary Item Box

Creates a new constant with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads MustOverride Function CreateConstant( _
       ByVal _displayName_ As String _
    ) As [ProjectConstant](topic4171.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim displayName As String
    Dim value As [ProjectConstant](topic4171.md)
     
    value = instance.CreateConstant(displayName)  
  
C#|   
---|---  
      
    
    public abstract [ProjectConstant](topic4171.md) CreateConstant( 
       string _displayName_
    )  
  
#### Parameters

 _displayName_
    The display name to assign to the constant.

#### Return Value

The newly created constant.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)   
[Overload List](topic4252.md)


