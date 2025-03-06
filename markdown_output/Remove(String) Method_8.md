Remove(String) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedCustomPropertyCollection Class](topic14812.md) > [Remove Method](topic14820.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the custom property to remove.

Glossary Item Box

Removes the custom property with the specified name from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedCustomPropertyCollection](topic14812.md)
    Dim name As String
    Dim value As Boolean
     
    value = instance.Remove(name)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the custom property to remove.

#### Return Value

True if the custom property was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedCustomPropertyCollection Class](topic14812.md)   
[ReleasedCustomPropertyCollection Members](topic14813.md)   
[Overload List](topic14820.md)


