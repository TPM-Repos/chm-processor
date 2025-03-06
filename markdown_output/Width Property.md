       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Width Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10830.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Condition Class](topic10804.md) : Width Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the width of the condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Property Width As Nullable(Of Double)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Condition](topic10804.md)
    Dim value As Nullable(Of Double)
     
    instance.Width = value
     
    value = instance.Width  
  
C#|   
---|---  
      
    
    public override Nullable<double> Width {get; set;}  
  
# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The value is less than [DriveWorks.EventFlow.ExecutableNodeBase.MIN_WIDTH](topic6975.md) or greater than [DriveWorks.EventFlow.ExecutableNodeBase.MAX_WIDTH](topic6972.md).  
  
# Remarks

Setting this to null (or Nothing in Visual Basic) will cause the condition to auto size.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Condition Class](topic10804.md)   
[Condition Members](topic10805.md)

©2024 DriveWorks Ltd. All Rights Reserved.
