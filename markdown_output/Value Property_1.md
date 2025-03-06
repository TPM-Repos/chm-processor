Value Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty<T> Class](topic10978.md) : Value Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the property value, see the remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Value As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty(Of T)](topic10978.md)
    Dim value As T
     
    instance.Value = value
     
    value = instance.Value  
  
C#|   
---|---  
      
    
    public T Value {get; set;}  
  
#### Property Value

The value of the property.

# Remarks

If the property is bound, the value returned will be a null reference for reference types, or the default value for value types.

If the property is bound and this property is set, the binding rule will be removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperty<T> Class](topic10978.md)   
[FlowProperty<T> Members](topic10979.md)


