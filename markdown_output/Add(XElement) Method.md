Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(XElement) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) > [Add Method](topic11473.md) : Add(XElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macroXml_
    The xElement containing the definition for the specification macro.

Glossary Item Box

Adds a new macro created from the given xElement. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _macroXml_ As XElement _
    ) As [SpecificationMacro](topic11429.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim macroXml As XElement
    Dim value As [SpecificationMacro](topic11429.md)
     
    value = instance.Add(macroXml)  
  
C#|   
---|---  
      
    
    public [SpecificationMacro](topic11429.md) Add( 
       XElement _macroXml_
    )  
  
#### Parameters

 _macroXml_
    The xElement containing the definition for the specification macro.

#### Return Value

The newly created macro.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)   
[Overload List](topic11473.md)


