       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RowHeight Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [DataTableControl Class](topic7864.md) : RowHeight Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the height value to apply to all rows in the data table, excluding the header row. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property RowHeight As Double  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DataTableControl](topic7864.md)
    Dim value As Double
     
    instance.RowHeight = value
     
    value = instance.RowHeight  
  
C#|   
---|---  
      
    
    public double RowHeight {get; set;}  
  
# Remarks

When this is 0 it is treated as an auto size value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataTableControl Class](topic7864.md)   
[DataTableControl Members](topic7865.md)


