import { GridCellKind } from "@glideapps/glide-data-grid"

export function getDEColumn(columns, col) {
    let c = columns[col];
    c.pos = col;
    return c;
}

export function getDERow(data, row) {
    return data[row];
}

export function locateCell(row, column) {
    if (Array.isArray(row)) {
        return row[column.pos];
    } else {
        return row[column.id];
    }
}

export function formatCell(value, column) {
    switch (column.type) {
        case "int":
        case "float":
            return {
                kind: GridCellKind.Number,
                data: value,
                displayData: value + "",
                readonly: false,
                allowOverlay: false
            }
        case "datetime":
        // value = moment format?
        case "str":
            return {
                kind: GridCellKind.Text,
                data: value,
                displayData: value,
                readonly: false,
                allowOverlay: true
            }
        case "bool":
            return {
                kind: GridCellKind.Boolean,
                data: value,
                readonly: false,
                // allowOverlay: true
            }
        default:
            return {
                kind: GridCellKind.Text,
                data: value,
                displayData: "type not specified in column definition"
            }
    };
};