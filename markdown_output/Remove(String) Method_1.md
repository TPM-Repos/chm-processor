Remove(String) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAnnotationCollection Class](topic14063.md) > [Remove Method](topic14072.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the annotation to remove.

Glossary Item Box

Removes the annotation with the specified name from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedAnnotationCollection](topic14063.md)
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
    The name of the annotation to remove.

#### Return Value

True if the annotation was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedAnnotationCollection Class](topic14063.md)   
[CapturedAnnotationCollection Members](topic14064.md)   
[Overload List](topic14072.md)


