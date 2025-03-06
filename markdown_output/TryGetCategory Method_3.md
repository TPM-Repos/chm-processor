TryGetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategory Class](topic4983.md) : TryGetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to get.

_itemCategory_
    Receives the named category if it was found, otherwise receives a null reference (Nothing in Visual Basic).

Glossary Item Box

Tries to get a category with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetCategory( _
       ByVal _name_ As String, _
       ByRef _itemCategory_ As [ProjectVariableCategory](topic4983.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategory](topic4983.md)
    Dim name As String
    Dim itemCategory As [ProjectVariableCategory](topic4983.md)
    Dim value As Boolean
     
    value = instance.TryGetCategory(name, itemCategory)  
  
C#|   
---|---  
      
    
    public bool TryGetCategory( 
       string _name_ ,
       ref [ProjectVariableCategory](topic4983.md) _itemCategory_
    )  
  
#### Parameters

 _name_
    The name of the category to get.
_itemCategory_
    Receives the named category if it was found, otherwise receives a null reference (Nothing in Visual Basic).

#### Return Value

True if the named category was found, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategory Class](topic4983.md)   
[ProjectVariableCategory Members](topic4984.md)


