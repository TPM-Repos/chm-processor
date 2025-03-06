       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRange(String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2853.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ExcelDocument Class](topic2834.md) > [SetRange Method](topic2852.md) : SetRange(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be driven.

_formula_
    Formula of the range.

Glossary Item Box

Sets/adds ranges to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetRange( _
       ByVal _name_ As String, _
       ByVal _formula_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExcelDocument](topic2834.md)
    Dim name As String
    Dim formula As String
     
    instance.SetRange(name, formula)  
  
C#|   
---|---  
      
    
    public void SetRange( 
       string _name_ ,
       string _formula_
    )  
  
#### Parameters

 _name_
    Name of the range to be driven.
_formula_
    Formula of the range.

# Remarks

A name must exactly equal Excel file's range name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExcelDocument Class](topic2834.md)   
[ExcelDocument Members](topic2835.md)   
[Overload List](topic2852.md)

©2024 DriveWorks Ltd. All Rights Reserved.
