       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14921.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureParameterCollection Class](topic14911.md) > [Remove Method](topic14919.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the additional feature parameter to remove.

Glossary Item Box

Removes the additional feature parameter with the specified name from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _address_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureParameterCollection](topic14911.md)
    Dim address As String
    Dim value As Boolean
     
    value = instance.Remove(address)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       string _address_
    )  
  
#### Parameters

 _address_
    The address of the additional feature parameter to remove.

#### Return Value

True if the additional feature parameter was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFeatureParameterCollection Class](topic14911.md)   
[ReleasedFeatureParameterCollection Members](topic14912.md)   
[Overload List](topic14919.md)

©2024 DriveWorks Ltd. All Rights Reserved.
