![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTypesFromLibraries Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2087.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : GetTypesFromLibraries Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_baseType_
    The type of a class from which the returned types must inherit, or an interface which the returned types must implement.

_attributes_
    An array of attributes which must be defined on the returned types, or a null reference if no attribute filtering is required.

Glossary Item Box

Gets types which inherit from the specified base type, or implement the specified interface. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTypesFromLibraries( _
       ByVal _baseType_ As Type, _
       ByVal _attributes_() As Type _
    ) As Type()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim baseType As Type
    Dim attributes() As Type
    Dim value() As Type
     
    value = instance.GetTypesFromLibraries(baseType, attributes)  
  
C#|   
---|---  
      
    
    Type[] GetTypesFromLibraries( 
       Type _baseType_ ,
       Type[] _attributes_
    )  
  
#### Parameters

 _baseType_
    The type of a class from which the returned types must inherit, or an interface which the returned types must implement.
_attributes_
    An array of attributes which must be defined on the returned types, or a null reference if no attribute filtering is required.

#### Return Value

An array of types meeting the specified filter.

# ![](dotnetimages/collapse.gif)Remarks

The base type must implement the [DriveWorks.Extensibility.IExtension](topic7152.md) interface to be discoverable using this method.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)

©2024 DriveWorks Ltd. All Rights Reserved.
