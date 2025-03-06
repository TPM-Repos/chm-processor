       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetCategoryCore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4947.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : SetCategoryCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_category_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Sub SetCategoryCore( _
       ByVal _category_ As [ProjectVariableCategory](topic4983.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim category As [ProjectVariableCategory](topic4983.md)
     
    instance.SetCategoryCore(category)  
  
C#|   
---|---  
      
    
    protected abstract void SetCategoryCore( 
       [ProjectVariableCategory](topic4983.md) _category_
    )  
  
#### Parameters

 _category_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)

©2024 DriveWorks Ltd. All Rights Reserved.
