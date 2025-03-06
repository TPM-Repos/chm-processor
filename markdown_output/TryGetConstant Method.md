TryGetConstant Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) : TryGetConstant Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the constant to retrieve.

_constant_
    A reference to a constant which will receive the constant.

Glossary Item Box

Gets the constant with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function TryGetConstant( _
       ByVal _displayName_ As String, _
       ByRef _constant_ As [ProjectConstant](topic4171.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim displayName As String
    Dim constant As [ProjectConstant](topic4171.md)
    Dim value As Boolean
     
    value = instance.TryGetConstant(displayName, constant)  
  
C#|   
---|---  
      
    
    public abstract bool TryGetConstant( 
       string _displayName_ ,
       ref [ProjectConstant](topic4171.md) _constant_
    )  
  
#### Parameters

 _displayName_
    The display name of the constant to retrieve.
_constant_
    A reference to a constant which will receive the constant.

#### Return Value

True if the constant is found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)


