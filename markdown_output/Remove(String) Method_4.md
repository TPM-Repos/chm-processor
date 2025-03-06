       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14212.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFeatureCollection Class](topic14201.md) > [Remove Method](topic14210.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the item to remove.

Glossary Item Box

Removes the item with the specified name from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFeatureCollection](topic14201.md)
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
    The name of the item to remove.

#### Return Value

True if the item was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFeatureCollection Class](topic14201.md)   
[CapturedFeatureCollection Members](topic14202.md)   
[Overload List](topic14210.md)

©2024 DriveWorks Ltd. All Rights Reserved.
