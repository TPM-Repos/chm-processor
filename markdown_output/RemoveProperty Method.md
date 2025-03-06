       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveProperty Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9438.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : RemoveProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control from which to remove the property.

_dynamicProperty_
    The property to remove from the control property list.

Glossary Item Box

Removes a dynamic property from the list of properties for the given control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub RemoveProperty( _
       ByVal _controlType_ As Type, _
       ByVal _dynamicProperty_ As [DynamicProperty](topic9398.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim dynamicProperty As [DynamicProperty](topic9398.md)
     
    [DynamicProperty](topic9398.md).RemoveProperty(controlType, dynamicProperty)  
  
C#|   
---|---  
      
    
    public static void RemoveProperty( 
       Type _controlType_ ,
       [DynamicProperty](topic9398.md) _dynamicProperty_
    )  
  
#### Parameters

 _controlType_
    The type of the control from which to remove the property.
_dynamicProperty_
    The property to remove from the control property list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)

©2024 DriveWorks Ltd. All Rights Reserved.
