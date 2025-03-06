       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveRange Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ExcelDocument Class](topic2834.md) : RemoveRange Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be removed from the drive list.

Glossary Item Box

Removes a range from the list of ranges to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveRange( _
       ByVal _name_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExcelDocument](topic2834.md)
    Dim name As String
     
    instance.RemoveRange(name)  
  
C#|   
---|---  
      
    
    public void RemoveRange( 
       string _name_
    )  
  
#### Parameters

 _name_
    Name of the range to be removed from the drive list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExcelDocument Class](topic2834.md)   
[ExcelDocument Members](topic2835.md)


