![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAttribute(Assembly,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7216.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) > [GetAttribute Method](topic7214.md) : GetAttribute(Assembly,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_assembly_
    The assembly from which to retrieve the attribute.

_createIfNotDefined_
    Determines whether an attribute is synthesized for assemblies which do not define one.

Glossary Item Box

Gets the [LibraryAttribute](topic7201.md) from the specified assembly. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetAttribute( _
       ByVal _assembly_ As Assembly, _
       ByVal _createIfNotDefined_ As Boolean _
    ) As [LibraryAttribute](topic7201.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim assembly As Assembly
    Dim createIfNotDefined As Boolean
    Dim value As [LibraryAttribute](topic7201.md)
     
    value = [LibraryAttribute](topic7201.md).GetAttribute(assembly, createIfNotDefined)  
  
C#|   
---|---  
      
    
    public static [LibraryAttribute](topic7201.md) GetAttribute( 
       Assembly _assembly_ ,
       bool _createIfNotDefined_
    )  
  
#### Parameters

 _assembly_
    The assembly from which to retrieve the attribute.
_createIfNotDefined_
    Determines whether an attribute is synthesized for assemblies which do not define one.

#### Return Value

An instance of the library attribute if it is applied to the specified assembly, otherwise a null reference (Nothing in Visual Basic).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)   
[Overload List](topic7214.md)

©2024 DriveWorks Ltd. All Rights Reserved.
