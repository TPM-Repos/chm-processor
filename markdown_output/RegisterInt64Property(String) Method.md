Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterInt64Property(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperties Class](topic10905.md) > [RegisterInt64Property Method](topic10935.md) : RegisterInt64Property(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

Glossary Item Box

Creates a new specification flow property which can store 64-bit integral data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterInt64Property( _
       ByVal _name_ As String _
    ) As [FlowProperty(Of Long)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperties](topic10905.md)
    Dim name As String
    Dim value As [FlowProperty(Of Long)](topic10978.md)
     
    value = instance.RegisterInt64Property(name)  
  
C#|   
---|---  
      
    
    public [FlowProperty<long>](topic10978.md) RegisterInt64Property( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the property.

#### Return Value

A new specification flow property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperties Class](topic10905.md)   
[FlowProperties Members](topic10906.md)   
[Overload List](topic10935.md)


