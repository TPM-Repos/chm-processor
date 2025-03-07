Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [GetComponent Method](topic3036.md) : GetComponent(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentPath_
    The fully qualified file path to the component.

Glossary Item Box

Gets the captured component with the specified file path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetComponent( _
       ByVal _componentPath_ As String _
    ) As [CapturedComponent](topic6147.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim componentPath As String
    Dim value As [CapturedComponent](topic6147.md)
     
    value = instance.GetComponent(componentPath)  
  
C#|   
---|---  
      
    
    public [CapturedComponent](topic6147.md) GetComponent( 
       string _componentPath_
    )  
  
#### Parameters

 _componentPath_
    The fully qualified file path to the component.

#### Return Value

The component with the specified file path if it is registered, otherwise a null reference.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The component type is not supported.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3036.md)


